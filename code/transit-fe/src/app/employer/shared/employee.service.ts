import { Injectable } from '@angular/core';

import { Employee } from './employee.model';

import { Observable, Subject } from 'rxjs';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Injectable()
export class EmployeeService {
  private employeesUrl = 'http://127.0.0.1:5000/employees';

  private employees = new Subject<Employee[]>();
  employees$ = this.employees.asObservable();
  employeeArray: Employee[] = [];



  initEmployees() {
    //getEmployees() currently returns all employees of all employers. 
    //Backend should be modified to only return employees of the logged in Employer who made this request. 
    //Admins should have another endpoint where they provide an Employer.Id in order to see employees of that Employer.
    this.getEmployees().subscribe(result => { this.employees.next(result); this.employeeArray = result });

    this.employees$ = this.employees.asObservable();
  }

  httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' })
  }

  constructor(
    private http: HttpClient) { }

  getEmployees(): Observable<Employee[]> {
    return this.http.get<Employee[]>(this.employeesUrl)
  }

  getEmployee(id: number): Observable<Employee> {
    const url = `${this.employeesUrl}/${id}`;
    return this.http.get<Employee>(url)
  }


  addEmployee(employee: Employee) {
    //We shouldn't need to send an employer id once we can find out who is sending this "add_employee" request from whoever is logged in
    //We might want to have two routes, one for Admins to use which can specify which Employer to add this Employee to, but typically 
    //if it's an Employer account adding an Employee it should go to the logged in account's Employee list
    employee.employer_id = 1;
    employee.success = false;
    return this.http.post<Employee>(this.employeesUrl, employee, this.httpOptions).subscribe(newEmployee => { this.employeeArray.push(newEmployee); this.employees.next(this.employeeArray); })
  }

  deleteEmployee(employee: Employee | number): Observable<Employee> {
    const id = typeof employee === 'number' ? employee : employee.id;
    const url = `${this.employeesUrl}/${id}`;

    return this.http.delete<Employee>(url, this.httpOptions)
  }

  updateEmployee(employee: Employee): Observable<any> {
    const id = typeof employee === 'number' ? employee : employee.id;
    const url = `${this.employeesUrl}/${id}`;
    return this.http.put(url, employee, this.httpOptions)
  }
}

