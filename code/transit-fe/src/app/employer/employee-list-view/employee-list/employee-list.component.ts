import { Component, OnInit, ViewChild } from '@angular/core';
import { Employee } from '../../shared/employee.model';
import { animate, state, style, transition, trigger } from '@angular/animations';
import { EmployeeService} from '../../shared/employee.service';
import { MatTableDataSource } from '@angular/material/table';
import { MatPaginator } from '@angular/material/paginator';
import { MatSort } from '@angular/material/sort';


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


  @ViewChild(MatPaginator) paginator: MatPaginator;
  @ViewChild(MatSort) sort: MatSort;

  employees = new MatTableDataSource<Employee>();
  displayedColumns: string[] = ["First Name", "Last Name", "Email"];
  columnsToDisplay: string[] = this.displayedColumns.slice();
  expandedEmployer: Employee | null;

  constructor(private employeeService: EmployeeService) {
    this.employeeService.employees$.subscribe(getEmployees => this.employees.data = getEmployees);
   }

   ngAfterViewInit() {
    this.employees.paginator = this.paginator;
    this.employees.sort = this.sort;
  }

  applyFilter(filterValue: string) {
    filterValue = filterValue.trim(); // Remove whitespace
    filterValue = filterValue.toLowerCase(); // Datasource defaults to lowercase matches
    this.employees.filter = filterValue;
  }

  ngOnInit(): void {
  }

}
