import { Component } from '@angular/core';
import { EmployerService } from './city-go-admin/shared/employer.service';
import { EmployeeService } from './employer/shared/employee.service';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],

  providers: [EmployerService, EmployeeService]

})
export class AppComponent {
  title = 'transit-fe';
}
