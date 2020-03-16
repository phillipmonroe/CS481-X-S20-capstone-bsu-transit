import { Component, OnInit } from '@angular/core';
import { Employer } from './shared/employer.model';
import { EmployerService } from './shared/employer.service';

@Component({
  selector: 'city-go-admin',
  templateUrl: './city-go-admin.component.html',
  styleUrls: ['./city-go-admin.component.css']
})
export class CityGoAdminComponent implements OnInit {
  
  employers: Employer[] = [];
  constructor(private employerService: EmployerService) {}

  ngOnInit() {
    // this.employerService.getEmployers()
    //   .then(employers => this.employers = employers);
    this.employerService.employers$.subscribe(employers => this.employers.push(employers));
  }

}