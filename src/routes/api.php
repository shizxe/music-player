<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\Product\ProductController;
use App\Http\Controllers\User\UserController;
use App\Http\Controllers\Blog\BlogController;

Route::apiResource('blogs', BlogController::class);
Route::apiResource('users', UserController::class);
Route::apiResource('products', ProductController::class);
