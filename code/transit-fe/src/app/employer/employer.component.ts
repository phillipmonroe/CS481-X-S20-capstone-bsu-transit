import { Component, OnInit } from '@angular/core';
import { EmployeeService } from './shared/employee.service';

@Component({
  selector: 'app-employer',
  templateUrl: './employer.component.html',
  styleUrls: ['./employer.component.css']
})
export class EmployerComponent implements OnInit {

  constructor(private employeeService: EmployeeService) {}
 

  ngOnInit(): void {
    this.employeeService.initEmployees();
  }

}