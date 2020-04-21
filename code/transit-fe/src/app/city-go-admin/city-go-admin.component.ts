import { Component, OnInit } from '@angular/core';
import {HttpClient, HttpErrorResponse, HttpHeaders} from '@angular/common/http';
import Auth0Client from '@auth0/auth0-spa-js/dist/typings/Auth0Client';
import { EmployerService } from './shared/employer.service';

@Component({
  selector: 'city-go-admin',
  templateUrl: './city-go-admin.component.html',
  styleUrls: ['./city-go-admin.component.css']
})
export class CityGoAdminComponent implements OnInit {
  
  constructor(private employerService: EmployerService) {
  }
  
  ngOnInit() {
    this.employerService.initEmployers();
  }

}
