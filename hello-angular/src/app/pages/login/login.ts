// src/app/pages/login/login.ts
import { Component } from '@angular/core';
import { AuthService } from '../../services/auth';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.html',
  styleUrls: ['./login.css']
})
export class LoginComponent {
  email = '';
  password = '';

  constructor(private authService: AuthService, private router: Router) {}

  onLogin(event: Event) {
    event.preventDefault();
    this.authService.login({ email: this.email, password: this.password }).subscribe({
      next: (res) => {
        this.authService.storeToken(res.access_token);
        this.router.navigate(['/']); // Navigate to home or dashboard
      },
      error: (err) => {
        alert('Login failed: ' + err.error?.message || 'Unknown error');
      }
    });
  }
}
