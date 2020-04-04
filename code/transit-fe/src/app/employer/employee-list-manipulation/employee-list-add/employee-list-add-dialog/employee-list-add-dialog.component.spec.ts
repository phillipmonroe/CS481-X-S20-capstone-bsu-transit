import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { EmployeeListAddDialogComponent } from './employee-list-add-dialog.component';

describe('EmployeeListAddDialogComponent', () => {
  let component: EmployeeListAddDialogComponent;
  let fixture: ComponentFixture<EmployeeListAddDialogComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ EmployeeListAddDialogComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(EmployeeListAddDialogComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
