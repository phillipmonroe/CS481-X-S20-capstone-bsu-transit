import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-add-employer',
  templateUrl: './add-employer.component.html',
  styleUrls: ['./add-employer.component.css']
})
export class AddEmployerComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
  }


  submit_onClick() {
    console.log('hello, submit button works')
  }
  clear_onClick() {
    console.log('hello, clear button works')
  }

}