import { Component, Input } from '@angular/core';
import { Employer } from '../shared/employer.model';
import { EmployerService } from '../shared/employer.service';

@Component({
  selector: 'admin-employer-list-view',
  templateUrl: './employer-list-view.component.html',
  styleUrls: ['./employer-list-view.component.css']
})
export class EmployerListViewComponent {
  
  constructor(private employerService: EmployerService) { }

  ngOnInit() {
  }

  @Input() employers: Employer;
}
