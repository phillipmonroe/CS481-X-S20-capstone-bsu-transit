import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CityGoAdminComponent } from './city-go-admin.component';

describe('CityGoAdminComponent', () => {
  let component: CityGoAdminComponent;
  let fixture: ComponentFixture<CityGoAdminComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [CityGoAdminComponent]
    })
      .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CityGoAdminComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
