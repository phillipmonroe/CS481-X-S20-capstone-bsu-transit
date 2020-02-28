import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { CityGoAdminComponent } from './city-go-admin/city-go-admin.component';
import { EmployerComponent } from './employer/employer.component';
import { ProfileComponent } from './profile/profile.component';
import { AuthGuard } from './auth.guard';


/**
 * --Add Component Paths Here--
 */
const routes: Routes = [
  {path: 'city-go-admin', component: CityGoAdminComponent },
  {path: 'employer', component: EmployerComponent },
  {path: 'profile', component: ProfileComponent, canActivate: [AuthGuard]}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
