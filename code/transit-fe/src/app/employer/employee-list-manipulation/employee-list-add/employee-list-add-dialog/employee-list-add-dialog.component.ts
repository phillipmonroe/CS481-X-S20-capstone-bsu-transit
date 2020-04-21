import { Component, Inject } from '@angular/core';
import { MatDialogRef, MAT_DIALOG_DATA } from '@angular/material/dialog';
import { Employee } from '../../../shared/employee.model';

@Component({
  selector: 'app-employee-list-add-dialog',
  templateUrl: './employee-list-add-dialog.component.html',
  styleUrls: ['./employee-list-add-dialog.component.css']
})
export class EmployeeListAddDialogComponent{

  constructor(
    public dialogRef: MatDialogRef<EmployeeListAddDialogComponent>,
    @Inject(MAT_DIALOG_DATA) public data: Employee) {}


  onNoClick(): void {
    this.dialogRef.close();
  }
}
