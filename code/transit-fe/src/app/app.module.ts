import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { MatTableModule } from '@angular/material/table';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatButtonModule } from '@angular/material/button';
import { MatButtonToggleModule } from '@angular/material/button-toggle';
import { MatDialogModule } from '@angular/material/dialog';
import { MatInputModule } from '@angular/material/input';
import { FormsModule } from '@angular/forms';
import { MatSortModule } from '@angular/material/sort';
import { MatPaginatorModule } from '@angular/material/paginator';
import { MatMenuModule } from '@angular/material/menu';
import { MatIconModule } from '@angular/material/icon';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { AdminTopBarComponent } from './admin-top-bar/admin-top-bar.component';
import { EmployerComponent } from './employer/employer.component';
import { NavBarComponent } from './nav-bar/nav-bar.component';
import { ProfileComponent } from './profile/profile.component';
import { CityGoAdminComponent } from './city-go-admin/city-go-admin.component';
import { EmployerListComponent } from './city-go-admin/employer-list-view/employer-list/employer-list.component';
import { EmployerListViewComponent } from './city-go-admin/employer-list-view/employer-list-view.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { EmployerListManipulationComponent } from './city-go-admin/employer-list-manipulation/employer-list-manipulation.component';
import { ListAddComponent } from './city-go-admin/employer-list-manipulation/list-add/list-add.component';
import { ListAddDialogComponent } from './city-go-admin/employer-list-manipulation/list-add/list-add-dialog/list-add-dialog.component';
import { AddEmployerComponent } from './add-employer/add-employer.component';
import { EmployeeListViewComponent } from './employer/employee-list-view/employee-list-view.component';
import { EmployeeListComponent } from './employer/employee-list-view/employee-list/employee-list.component';
import { EmployeeListManipulationComponent } from './employer/employee-list-manipulation/employee-list-manipulation.component';
import { EmployeeListAddComponent } from './employer/employee-list-manipulation/employee-list-add/employee-list-add.component';
import { EmployeeListAddDialogComponent } from './employer/employee-list-manipulation/employee-list-add/employee-list-add-dialog/employee-list-add-dialog.component';
import { AddEmployeeComponent } from './add-employee/add-employee.component';

@NgModule({
  declarations: [
    AppComponent,
    CityGoAdminComponent,
    AdminTopBarComponent,
    EmployerComponent,
    NavBarComponent,
    ProfileComponent,
    EmployerListComponent,
    EmployerListViewComponent,
    EmployerListManipulationComponent,
    ListAddComponent,
    ListAddDialogComponent,
    AddEmployerComponent,
    AddEmployeeComponent,
    EmployeeListViewComponent,
    EmployeeListComponent,
    EmployeeListManipulationComponent,
    EmployeeListAddComponent,
    EmployeeListAddDialogComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    MatTableModule,
    MatToolbarModule,
    MatButtonToggleModule,
    MatButtonModule,
    MatDialogModule,
    MatInputModule,
    FormsModule,
    MatPaginatorModule,
    MatSortModule,
    MatMenuModule,
    MatIconModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
