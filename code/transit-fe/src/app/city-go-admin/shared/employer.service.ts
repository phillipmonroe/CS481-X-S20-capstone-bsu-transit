import { Injectable } from '@angular/core';
import { Employer } from './employer.model';
import { Subject, Observable } from 'rxjs';

@Injectable()
export class EmployerService {
  
  private employers = new Subject<Employer[]>();
  employers$ = this.employers.asObservable();

  addEmployer(employer: Employer[]) {
    this.employers.next(employer);
  }

  public getEmployersShared(): Observable<Employer[]> {
    return this.employers.asObservable();
  }
}