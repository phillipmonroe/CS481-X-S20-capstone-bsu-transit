import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, Subject } from 'rxjs';
import { Employer } from './employer.model';

/**
 * @author Phillip Monroe
 * @author Colin Beckley
 * @author Desmond Porth
 */
@Injectable({ providedIn: 'root' })
export class EmployerService {

  // This is the url to the backend where we will send requests
  private employersUrl = 'http://127.0.0.1:5000/employers';


  private employers = new Subject<Employer[]>();
  employers$ = this.employers.asObservable();
  employerArray: Employer[] = [];

  initEmployers() {
    this.getEmployers().subscribe(result => { this.employers.next(result); this.employerArray = result });
    this.employers$ = this.employers.asObservable();
  }

  // any future authorization needed to access the backend would be placed in here
  httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' })
  };

  constructor(
    private http: HttpClient) { }

  /**
   * Get all employers in the databse
   */
  getEmployers(): Observable<Employer[]> {
    return this.http.get<Employer[]>(this.employersUrl)
  }

  /**
   * Get Employer with a specified id
   * 
   * @param id of the employer you would like 
   */
  getEmployer(id: number): Observable<Employer> {
    const url = `${this.employersUrl}/${id}`;
    return this.http.get<Employer>(url)
  }

  /**
   * Add a new employer
   * 
   * @param employer employer object to add
   */
  addEmployer(employer: Employer) {
    return this.http.post<Employer>(this.employersUrl, employer, this.httpOptions).subscribe(newEmployer => { this.employerArray.push(newEmployer); this.employers.next(this.employerArray); })
  }

  /**
   * Delete the specified employer
   * TODO: use somewhere
   * 
   * @param employer id of employer or the employer object
   */
  deleteEmployer(employer: Employer | number): Observable<Employer> {
    const id = typeof employer === 'number' ? employer : employer.id;
    const url = `${this.employersUrl}/${id}`;

    return this.http.delete<Employer>(url, this.httpOptions)
  }

  /**
   * Updates the specified employer
   * TODO: use somewhere
   * 
   * @param employer id of employer or the employer object
   */
  updateEmployer(employer: Employer): Observable<any> {
    const id = typeof employer === 'number' ? employer : employer.id;
    const url = `${this.employersUrl}/${id}`;
    return this.http.put(url, employer, this.httpOptions)
  }
}