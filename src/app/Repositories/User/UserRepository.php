<?php
declare(strict_types=1);

namespace App\Repositories\User;

use App\Models\User;

class UserRepository implements UserRepositoryInterface
{
    public function __construct(private User $model) {}

    public function getAll(): array
    {
        return $this->model->all()->toArray();
    }

    public function findById(int $id): array
    {
        return $this->model->findOrFail($id)->toArray();
    }

    public function create(array $data): array
    {
        return $this->model->create($data)->toArray();
    }

    public function update(int $id, array $data): array
    {
        $record = $this->model->findOrFail($id);
        $record->update($data);

        return $record->toArray();
    }

    public function delete(int $id): void
    {
        $this->model->findOrFail($id)->delete();
    }
}