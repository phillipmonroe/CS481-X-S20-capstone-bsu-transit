import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { EmployerListManipulationComponent } from './employer-list-manipulation.component';

describe('EmployerListManipulationComponent', () => {
  let component: EmployerListManipulationComponent;
  let fixture: ComponentFixture<EmployerListManipulationComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ EmployerListManipulationComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(EmployerListManipulationComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
