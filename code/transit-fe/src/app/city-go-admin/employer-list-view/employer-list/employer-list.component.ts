import { Component, Input } from '@angular/core';
import { Employer } from '../../shared/employer.model';
import {animate, state, style, transition, trigger} from '@angular/animations';

@Component({
  selector: 'admin-employer-list',
  templateUrl: './employer-list.component.html',
  styleUrls: ['./employer-list.component.css'],
  animations: [
    trigger('detailExpand', [
      state('collapsed', style({height: '0px', minHeight: '0'})),
      state('expanded', style({height: '*'})),
      transition('expanded <=> collapsed', animate('225ms cubic-bezier(0.4, 0.0, 0.2, 1)')),
    ]),
  ],
})
export class EmployerListComponent {

  constructor() { }

  ngOnInit(): void {
    
  }

  @Input() employers: Employer;
  displayedColumns: string[] = ["id", "name", "maxEmployees", "description"];
  expandedElement: Employer | null;

}
