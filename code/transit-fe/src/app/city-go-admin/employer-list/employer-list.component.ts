import { Component, OnInit, Input } from '@angular/core';
import { Employer } from '../shared/employer.model';

@Component({
  selector: 'admin-employer-list',
  templateUrl: './employer-list.component.html',
  styleUrls: ['./employer-list.component.css']
})
export class EmployerListComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
    
  }

  @Input() employer: Employer;

}
