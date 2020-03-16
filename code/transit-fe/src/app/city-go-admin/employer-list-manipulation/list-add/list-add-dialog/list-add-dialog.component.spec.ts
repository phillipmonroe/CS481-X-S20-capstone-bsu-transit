import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ListAddDialogComponent } from './list-add-dialog.component';

describe('ListAddDialogComponent', () => {
  let component: ListAddDialogComponent;
  let fixture: ComponentFixture<ListAddDialogComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ListAddDialogComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ListAddDialogComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
