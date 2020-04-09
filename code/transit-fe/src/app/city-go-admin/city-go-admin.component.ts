import { Component, OnInit } from '@angular/core';
import {HttpClient, HttpErrorResponse, HttpHeaders} from '@angular/common/http';
import Auth0Client from '@auth0/auth0-spa-js/dist/typings/Auth0Client';
@Component({
  selector: 'city-go-admin',
  templateUrl: './city-go-admin.component.html',
  styleUrls: ['./city-go-admin.component.css']
})
export class CityGoAdminComponent implements OnInit {
  
  constructor() {
    const httpOptions = {
      headers: new HttpHeaders({
        'Authorization': `Bearer ${Auth0Client.getAccessToken()}`
      })
    };
    console.log(httpOptions);
  }

  ngOnInit() {
  }

}