import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-admin-top-bar',
  templateUrl: './admin-top-bar.component.html',
  styleUrls: ['./admin-top-bar.component.css']
})
export class AdminTopBarComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
  }

  add_rmv_onClick() {
    console.log('hello, add/rmv button works')
  }

}
