import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PersonnelLoanComponent } from './personnel-loan.component';

describe('PersonnelLoanComponent', () => {
  let component: PersonnelLoanComponent;
  let fixture: ComponentFixture<PersonnelLoanComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PersonnelLoanComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(PersonnelLoanComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
