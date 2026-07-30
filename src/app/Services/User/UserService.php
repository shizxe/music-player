<?php
declare(strict_types=1);

namespace App\Services\User;

use App\Repositories\User\UserRepositoryInterface;

class UserService implements UserServiceInterface
{
    public function __construct(private UserRepositoryInterface $repository) {}

    public function getAll(): array
    {
        return $this->repository->getAll();
    }

    public function getById(int $id): array
    {
        return $this->repository->findById($id);
    }

    public function create(array $data): array
    {
        return $this->repository->create($data);
    }

    public function update(int $id, array $data): array
    {
        return $this->repository->update($id, $data);
    }

    public function delete(int $id): void
    {
        $this->repository->delete($id);
    }
}