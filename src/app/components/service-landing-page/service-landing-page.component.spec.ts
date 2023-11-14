import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ServiceLandingPageComponent } from './service-landing-page.component';

describe('ServiceLandingPageComponent', () => {
  let component: ServiceLandingPageComponent;
  let fixture: ComponentFixture<ServiceLandingPageComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ServiceLandingPageComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ServiceLandingPageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
