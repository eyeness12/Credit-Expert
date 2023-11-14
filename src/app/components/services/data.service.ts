import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

interface ApiResponse {
  response: string;
}

@Injectable({
  providedIn: 'root'
})
export class DataService {
  private apiUrl = 'http://127.0.0.1:5000/v1/personnel_credit';
  private apiUrl2 ='http://127.0.0.1:5000/v1/business_credit';
  constructor(private http: HttpClient) { }
  postData(info: any) :Observable<ApiResponse> {
    
    return this.http.post<ApiResponse>(this.apiUrl, info);
  }
  postDataE(info: any) :Observable<ApiResponse> {
    
    return this.http.post<ApiResponse>(this.apiUrl2, info);
  }
}
