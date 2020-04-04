import { Injectable } from '@angular/core';

import { Employee } from './employee.model';
import { Subject } from 'rxjs';
import { EMPLOYEES } from './mock-employees';

@Injectable()
export class EmployeeService {
  private employees = new Subject<Employee[]>();
  employees$ = this.employees.asObservable();


  addEmployee(employee: Employee[]) {
    this.employees.next(employee);
  }

  initEmployees(){

    this.employees.next(EMPLOYEES);
    this.employees$ = this.employees.asObservable();
  }
}
