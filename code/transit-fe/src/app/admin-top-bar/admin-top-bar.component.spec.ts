import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { AdminTopBarComponent } from './admin-top-bar.component';

describe('AdminTopBarComponent', () => {
  let component: AdminTopBarComponent;
  let fixture: ComponentFixture<AdminTopBarComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [AdminTopBarComponent]
    })
      .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(AdminTopBarComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
