import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-employer-top-bar',
  templateUrl: './employer-top-bar.component.html',
  styleUrls: ['./employer-top-bar.component.css']
})
export class EmployerTopBarComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
  }

  add_rmv_onClick(){
    console.log('hello, add/rmv button works')
}

}
