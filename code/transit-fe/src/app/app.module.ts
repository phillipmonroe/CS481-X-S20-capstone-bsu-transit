import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { MatTableModule } from '@angular/material/table';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatButtonModule } from '@angular/material/button';
import { MatButtonToggleModule } from '@angular/material/button-toggle';
import { MatDialogModule } from '@angular/material/dialog';
import { MatInputModule } from '@angular/material/input';
import { FormsModule } from '@angular/forms';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { AdminTopBarComponent } from './admin-top-bar/admin-top-bar.component';
import { EmployerComponent } from './employer/employer.component';
import { EmployerTopBarComponent } from './employer-top-bar/employer-top-bar.component';
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

@NgModule({
  declarations: [
    AppComponent,
    CityGoAdminComponent,
    AdminTopBarComponent,
    EmployerComponent,
    EmployerTopBarComponent,
    NavBarComponent,
    ProfileComponent,
    EmployerListComponent,
    EmployerListViewComponent,
    EmployerListManipulationComponent,
    ListAddComponent,
    ListAddDialogComponent,
    AddEmployerComponent
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
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
