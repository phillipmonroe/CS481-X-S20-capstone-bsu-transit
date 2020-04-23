import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { CityGoAdminComponent } from './city-go-admin/city-go-admin.component';
import { EmployerComponent } from './employer/employer.component';
import { ProfileComponent } from './profile/profile.component';
import { AuthGuard } from './auth.guard';
import { AddEmployerComponent } from './add-employer/add-employer.component';
import { AddEmployeeComponent } from './add-employee/add-employee.component';
import { HTTP_INTERCEPTORS } from '@angular/common/http';
import { InterceptorService } from './interceptor.service';

/**
 * --Add Component Paths Here--
 */
const routes: Routes = [
  { path: 'city-go-admin', component: CityGoAdminComponent, canActivate: [AuthGuard] },
  { path: 'employer', component: EmployerComponent, canActivate: [AuthGuard] },
  { path: 'profile', component: ProfileComponent, canActivate: [AuthGuard] },
  { path: 'add-employer', component: AddEmployerComponent, canActivate: [AuthGuard] },
  { path: 'add-employee', component: AddEmployeeComponent, canActivate: [AuthGuard] }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
  providers: [
    {
      provide: HTTP_INTERCEPTORS,
      useClass: InterceptorService,
      multi: true
    }
  ]
})
export class AppRoutingModule { }
