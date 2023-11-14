import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { DataService } from '../services/data.service';
import gsap from 'gsap';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-business',
  templateUrl: './business.component.html',
  styleUrls: ['./business.component.css']
})

export class BusinessComponent {
  starShine: any;
  tl: any;
  add_e: FormGroup | any;
  result: any;
  submitted = false;
  response!:string
  
  constructor(private fb: FormBuilder, private myservice:DataService) {}
  
  test:boolean=false;
  E_name:string ='';
  E_EBE:any=0;
  E_ET:any=0;
  E_CP:any=0;
  E_TA:any=0;
  E_RD:any=0;
  E_FF:any=0;
  E_CA:any=0;
  E_FP:any=0;
  E_VA:any=0;

  onSubmit() {
    var val={
      EBE: this.E_EBE,
      ET:  this.E_ET,
      CP:  this.E_CP,
      TA:  this.E_TA,
      RD: this. E_RD,
      FF: this.E_FF,
      CA:  this.E_CA,
      FP : this.E_FP,
      VA : this.E_VA
    }
    console.log(val)
    this.myservice.postDataE(val).subscribe( (data) => {
      this.result=data.response
      console.log("values",data);
    }, error => {
      console.error('Erreur lors de la requête :', error);
    });
    this.submitted=true; 
  
  }

  

  ngOnInit() {
    this.tl = gsap.timeline()
    .set('svg', {opacity:1})
    .set('.scratches', {rotation:70, x:450, y:-10})
    .set('#tri2', {scale:0.5})
    .from('#cardMask rect', {scale:0, rotation:-20, duration:2, transformOrigin:'50% 50%', ease:'expo.inOut'}, 0)
    .to('#tri1', {motionPath: {
        path: "#midC",
        align: "#midC",
        alignOrigin: [0.5,0.5],
        autoRotate: true,
        start: 1,
        end: 0
      }, duration:6, repeat:-1, ease:'none', repeatDelay:1}, 0.5)
    .to('#tri2', {motionPath: {
        path: "#innerC",
        align: "#innerC",
        alignOrigin: [0.5,0.5],
        autoRotate: true,
        start: 0,
        end: 1
      }, duration:5, repeat:-1, ease:'none', repeatDelay:1}, 1.5)
    .from('.coil', {attr:{'stroke-dashoffset':(i)=>(i==1)?-28:28}, ease:'none', duration:1, repeat:-1}, 1)
    .fromTo('#orb1', {y:160}, {y:-20, ease:'circ', repeat:-1, yoyo:true, duration:1}, 0.8)
    .from('.logoPt', {x:(i)=>[18,-10][i], duration:1.2, ease:'expo.inOut'}, 0.9)
    .from('svg text', {x:-40, duration:1.1, ease:'expo.inOut', stagger:0.2}, 1)
    .from('.txtBox', {scaleX:0, transformOrigin:'100% 0', duration:1.1, ease:'expo.inOut', stagger:0.2}, 1)
    .fromTo('#wave1', {x:0, y:0},{duration:5, x:-701, y:815, repeat:-1, ease:'none'}, 0)
    .fromTo('#wave2', {x:0, y:0},{duration:6, x:804, y:-917, repeat:-1, ease:'none', onRepeat:()=>this.starShine.play(0)}, 0)

    this.starShine = gsap.timeline()
    .set('#star', {scale:0, transformOrigin:'50% 50%', x:2, y:10})
    .to('#star', {scale:1, repeat:1, yoyo:true, yoyoEase:true, duration:0.4, ease:'power4'}, 0)
    .fromTo('#star', {rotate:-20},{rotate:120, duration:0.8, ease:'none'}, 0)
  }
}
