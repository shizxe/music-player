<?php
declare(strict_types=1);

namespace App\Repositories\User;

interface UserRepositoryInterface
{
    public function getAll(): array;

    public function findById(int $id): array;

    public function create(array $data): array;

    public function update(int $id, array $data): array;

    public function delete(int $id): void;
}