import { Injectable } from '@angular/core';

import { EMPLOYERS } from './mock-employers';
import { Employer } from './employer.model';
import { Subject } from 'rxjs';

@Injectable()
export class EmployerService {
  
  private employers = new Subject<Employer>();
  employers$ = this.employers.asObservable();

  getEmployers() {
    return Promise.resolve(EMPLOYERS);
  }

  addEmployer(employer: Employer) {
    this.employers.next(employer);
  }

  getEmployersShared() {
    return this.employers;
  }
}