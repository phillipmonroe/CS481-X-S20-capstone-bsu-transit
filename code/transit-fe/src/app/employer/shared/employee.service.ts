import { Injectable } from '@angular/core';

import { Employee } from './employee.model';
import { EMPLOYEES } from './mock-employees';


import { Observable, Subject } from 'rxjs';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Injectable()
export class EmployeeService {
  private employeesUrl = 'http://127.0.0.1:5000/employees';

  private employees = new Subject<Employee[]>();
  employees$ = this.employees.asObservable();
  employeeArray: Employee[] = [];

 

  initEmployees(){
    this.getEmployees().subscribe(result => {this.employees.next(result); this.employeeArray = result});

    this.employees$ = this.employees.asObservable();
  }

  httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' })
  }

  constructor(
    private http: HttpClient) { }

  getEmployees (): Observable<Employee[]> {
    return this.http.get<Employee[]>(this.employeesUrl)
  }

  getEmployee(id: number): Observable<Employee> {
    const url = `${this.employeesUrl}/${id}`;
    return this.http.get<Employee>(url)
  }


  addEmployee(employee: Employee) {
    employee.employer_id = 1;
    employee.success = false;
    return this.http.post<Employee>(this.employeesUrl, employee, this.httpOptions).subscribe(newEmployee => {this.employeeArray.push(newEmployee); this.employees.next(this.employeeArray);})
  }

  deleteEmployee (employee: Employee | number): Observable<Employee> {
    const id = typeof employee === 'number' ? employee : employee.id;
    const url = `${this.employeesUrl}/${id}`;

    return this.http.delete<Employee>(url, this.httpOptions)
  }

  updateEmployee (employee: Employee): Observable<any> {
    const id = typeof employee === 'number' ? employee : employee.id;
    const url = `${this.employeesUrl}/${id}`;
    return this.http.put(url, employee, this.httpOptions)
  }
}

