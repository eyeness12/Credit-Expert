import { PersonnelLoanComponent } from './components/personnel-loan/personnel-loan.component';
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HeroComponent } from './components/hero/hero.component';
import { ServiceLandingPageComponent } from './components/service-landing-page/service-landing-page.component';
import { BusinessComponent } from './components/business/business.component';

const routes: Routes = [
  {
    path: 'hero', component:HeroComponent
  },
  {
    path: 'service-landing-page' , component: ServiceLandingPageComponent
  },
  {
    path: 'personnel-loan' , component: PersonnelLoanComponent
  },
  {
    path: 'business', component: BusinessComponent
  },
  { path: '', redirectTo: '/hero', pathMatch: 'full' }

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
