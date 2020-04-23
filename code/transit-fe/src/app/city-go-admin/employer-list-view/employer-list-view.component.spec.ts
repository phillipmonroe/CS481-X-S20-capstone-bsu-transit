import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { EmployerListViewComponent } from './employer-list-view.component';

describe('EmployerListViewComponent', () => {
  let component: EmployerListViewComponent;
  let fixture: ComponentFixture<EmployerListViewComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [EmployerListViewComponent]
    })
      .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(EmployerListViewComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
