<?php
declare(strict_types=1);

namespace App\Services\Product;

interface ProductServiceInterface
{
    public function getAll(): array;

    public function getById(int $id): array;

    public function create(array $data): array;

    public function update(int $id, array $data): array;

    public function delete(int $id): void;
}