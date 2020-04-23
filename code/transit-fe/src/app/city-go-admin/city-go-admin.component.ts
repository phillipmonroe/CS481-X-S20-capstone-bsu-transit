import { Component, OnInit } from '@angular/core';
import {HttpClient, HttpErrorResponse, HttpHeaders} from '@angular/common/http';
import Auth0Client from '@auth0/auth0-spa-js/dist/typings/Auth0Client';
import { EmployerService } from './shared/employer.service';
import { Router } from "@angular/router";
import { AuthService } from '../auth.service';

@Component({
  selector: 'city-go-admin',
  templateUrl: './city-go-admin.component.html',
  styleUrls: ['./city-go-admin.component.css']
})
export class CityGoAdminComponent implements OnInit {

  constructor(private employerService: EmployerService, private router: Router, private auth: AuthService) {
    if (auth.userProfile$.source['_value']['https://any-namespace/roles'] != 'admin') {
      this.router.navigate(['employer']);
    }
  }
  ngOnInit() {
    this.employerService.initEmployers();
  }

}
