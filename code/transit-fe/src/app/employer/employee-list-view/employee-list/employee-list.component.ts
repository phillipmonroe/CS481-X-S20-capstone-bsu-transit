import { Component, OnInit } from '@angular/core';
import { Employee } from '../../shared/employee.model';
import { animate, state, style, transition, trigger } from '@angular/animations';
import { EmployeeService} from '../../shared/employee.service';
import { MatTableDataSource } from '@angular/material/table';


@Component({
  selector: 'app-employee-list',
  templateUrl: './employee-list.component.html',
  styleUrls: ['./employee-list.component.css'],
  animations: [
    trigger('detailExpand', [
      state('collapsed', style({height: '0px', minHeight: '0'})),
      state('expanded', style({height: '*'})),
      transition('expanded <=> collapsed', animate('225ms cubic-bezier(0.4, 0.0, 0.2, 1)')),
    ]),
  ],  
})
export class EmployeeListComponent implements OnInit{

  employees = new MatTableDataSource<Employee>();
  displayedColumns: string[] = ["firstName", "lastName", "email"];
  columnsToDisplay: string[] = this.displayedColumns.slice();
  expandedEmployer: Employee | null;

  constructor(private employeeService: EmployeeService) {
    this.employeeService.employees$.subscribe(getEmployees => this.employees.data = getEmployees);
   }

  ngOnInit(): void {
  }

}
