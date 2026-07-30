<?php
declare(strict_types=1);

namespace App\Providers;

use Illuminate\Support\ServiceProvider;

class RepositoryServiceProvider extends ServiceProvider
{
    public function register(): void
    {
        $this->app->bind(
            App\Repositories\Blog\BlogRepositoryInterface::class,
            App\Repositories\Blog\BlogRepository::class
        );

        $this->app->bind(
            App\Services\Blog\BlogServiceInterface::class,
            App\Services\Blog\BlogService::class
        );

        $this->app->bind(
            App\Repositories\User\UserRepositoryInterface::class,
            App\Repositories\User\UserRepository::class
        );

        $this->app->bind(
            App\Services\User\UserServiceInterface::class,
            App\Services\User\UserService::class
        );

        $this->app->bind(
            App\Repositories\Product\ProductRepositoryInterface::class,
            App\Repositories\Product\ProductRepository::class
        );

        $this->app->bind(
            App\Services\Product\ProductServiceInterface::class,
            App\Services\Product\ProductService::class
        );

    }

    public function boot(): void
    {
        //
    }
}