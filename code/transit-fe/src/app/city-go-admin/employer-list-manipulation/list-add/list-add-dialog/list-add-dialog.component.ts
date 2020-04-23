import { Component, Inject } from '@angular/core';
import { MatDialogRef, MAT_DIALOG_DATA } from '@angular/material/dialog';
import { Employer } from '../../../shared/employer.model';


@Component({
  selector: 'admin-list-add-dialog',
  templateUrl: './list-add-dialog.component.html',
  styleUrls: ['./list-add-dialog.component.css']
})
export class ListAddDialogComponent {

  constructor(
    public dialogRef: MatDialogRef<ListAddDialogComponent>,
    @Inject(MAT_DIALOG_DATA) public data: Employer) { }


  onNoClick(): void {
    this.dialogRef.close();
  }
}
