import { Component, Output, ViewChild } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { EmployeeListAddDialogComponent } from './employee-list-add-dialog/employee-list-add-dialog.component';
import { Employee } from '../../shared/employee.model';
import {MatSort} from '@angular/material/sort';
import { EmployeeService } from '../../shared/employee.service';
 


@Component({
  selector: 'app-employee-list-add',
  templateUrl: './employee-list-add.component.html',
  styleUrls: ['./employee-list-add.component.css']
})
export class EmployeeListAddComponent {

  

  employees: Employee[] = [];
  employee: Employee = { firstName: null, lastName: null, email: null};

  constructor(public dialog: MatDialog,private employeeService: EmployeeService) {

    this.employeeService.employees$.subscribe(addEmployees => this.employees = addEmployees);

  }

  ngOnInit(): void {
    
  }

  openDialog(): void {
    const dialogRef = this.dialog.open(EmployeeListAddDialogComponent, {
      width: '250px',
      data: this.employee
    });

    dialogRef.afterClosed().subscribe(result => {
      
      this.employees.push(this.employee);
      
      
      this.employeeService.addEmployee(this.employees);
      result = null;
      this.employee = { firstName: null, lastName: null, email: null};
    });
  }
}