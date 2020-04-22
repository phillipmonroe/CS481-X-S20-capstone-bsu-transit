import { Component, Output, ViewChild } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { EmployeeListAddDialogComponent } from './employee-list-add-dialog/employee-list-add-dialog.component';
import { Employee } from '../../shared/employee.model';
import {MatSort} from '@angular/material/sort';
import { EmployeeService } from '../../shared/employee.service';
import { HttpClient } from '@angular/common/http';
import {AuthService} from '../../../auth.service';




@Component({
  selector: 'app-employee-list-add',
  templateUrl: './employee-list-add.component.html',
  styleUrls: ['./employee-list-add.component.css']
})
export class EmployeeListAddComponent {

  uploadedFiles: Array <File>;

  employees: Employee[] = [];
  employee: Employee = { "id": null, "name": null, "email": null, "employer_id": null, "success": null };

  constructor(public dialog: MatDialog,
              private employeeService: EmployeeService,
              private http: HttpClient,
              public auth: AuthService) {

    this.employeeService.employees$.subscribe(addEmployees => this.employees = addEmployees);

  }

  // tslint:disable-next-line:use-lifecycle-interface
  ngOnInit(): void {

  }

    fileChange(element): void {
      this.uploadedFiles = element.target.files;
  }

  clear() {
    this.uploadedFiles = null;
  }

  upload(profile): void {
    const formData = new FormData();
    // tslint:disable-next-line:prefer-for-of
    for (let i = 0; i < this.uploadedFiles.length; i++) {
        formData.append('uploads[]', this.uploadedFiles[i], this.uploadedFiles[i].name);
    }
    formData.append('user', profile.email)
    this.http.post('http://localhost:5000/upload', formData)
    .subscribe((response) => {
         console.log('response received is ', response);
    });
}

  openDialog(): void {
    const dialogRef = this.dialog.open(EmployeeListAddDialogComponent, {
      width: '250px',
      data: this.employee
    });

    dialogRef.afterClosed().subscribe(result => {

      this.employeeService.addEmployee(this.employee);
      result = null;
      this.employee = { "id": null, "name": null, "email": null, "employer_id": null, "success": null };
    });
  }
}
