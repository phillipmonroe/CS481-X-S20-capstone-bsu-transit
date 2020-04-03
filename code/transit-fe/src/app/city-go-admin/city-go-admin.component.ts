import { Component, OnInit } from '@angular/core';
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