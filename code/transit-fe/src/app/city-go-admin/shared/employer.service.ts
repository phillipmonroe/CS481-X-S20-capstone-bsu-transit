import { Injectable } from '@angular/core';
import { Employer } from './employer.model';
import { Subject } from 'rxjs';
import { EMPLOYERS } from './mock-employers';
@Injectable()
export class EmployerService {
  
  private employers = new Subject<Employer[]>();
  employers$ = this.employers.asObservable();

  initEmployers() {
    this.employers.next(EMPLOYERS);
    this.employers$ = this.employers.asObservable();
  }
  
  addEmployer(employer: Employer[]) {
    this.employers.next(employer);
  }
}