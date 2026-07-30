<?php
declare(strict_types=1);

namespace App\Services\Blog;

use App\Repositories\Blog\BlogRepositoryInterface;

class BlogService implements BlogServiceInterface
{
    public function __construct(private BlogRepositoryInterface $repository) {}

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