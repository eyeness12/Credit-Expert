import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule,ReactiveFormsModule } from '@angular/forms';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HeroComponent } from './components/hero/hero.component';
import { NavbarComponent } from './components/navbar/navbar.component';
import { ServiceLandingPageComponent } from './components/service-landing-page/service-landing-page.component';
import { PersonnelLoanComponent } from './components/personnel-loan/personnel-loan.component';
import { BusinessComponent } from './components/business/business.component';
import { DataService } from './components/services/data.service';
import { HttpClient, HttpClientModule } from '@angular/common/http';

@NgModule({
  declarations: [
    AppComponent,
    HeroComponent,
    NavbarComponent,
    ServiceLandingPageComponent,
    PersonnelLoanComponent,
    BusinessComponent,
    
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    ReactiveFormsModule,
    HttpClientModule
  ],
  providers: [DataService ],
  bootstrap: [AppComponent]
})
export class AppModule { }
