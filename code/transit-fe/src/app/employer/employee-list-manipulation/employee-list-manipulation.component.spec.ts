import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { EmployeeListManipulationComponent } from './employee-list-manipulation.component';

describe('EmployeeListManipulationComponent', () => {
  let component: EmployeeListManipulationComponent;
  let fixture: ComponentFixture<EmployeeListManipulationComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [EmployeeListManipulationComponent]
    })
      .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(EmployeeListManipulationComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
