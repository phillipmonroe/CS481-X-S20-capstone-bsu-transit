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

  submit_onClick(){
    console.log('hello, submit button works')
    }
    clear_onClick(){
    console.log('hello, clear button works')
    }

}
