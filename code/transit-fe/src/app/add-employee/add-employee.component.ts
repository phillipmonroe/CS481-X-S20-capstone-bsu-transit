import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-add-employee',
  templateUrl: './add-employee.component.html',
  styleUrls: ['./add-employee.component.css']
})
export class AddEmployeeComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
  }

  submit_employee_onClick(){
    console.log('hello, submit employee button works')
    }

  submit_bulk_onClick(){
    console.log('hello, submit bulk button works')
    }
    clear_onClick(){
    console.log('hello, clear button works')
    }

}
