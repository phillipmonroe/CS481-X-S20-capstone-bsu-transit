import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { EmployeeListAddComponent } from './employee-list-add.component';

describe('EmployeeListAddComponent', () => {
  let component: EmployeeListAddComponent;
  let fixture: ComponentFixture<EmployeeListAddComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [EmployeeListAddComponent]
    })
      .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(EmployeeListAddComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
