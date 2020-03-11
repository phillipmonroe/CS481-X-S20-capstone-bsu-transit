import { Injectable } from '@angular/core';

import { EMPLOYERS } from './mock-employers';

@Injectable()
export class EmployerService {
  getEmployers() {
    return Promise.resolve(EMPLOYERS);
  }
}